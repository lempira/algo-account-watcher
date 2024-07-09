import { PropsWithChildren, Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

interface SectionErrorSuspenseProps {
  errorMsg: string;
}

export const ComponentErrorSuspense = ({
  errorMsg,
  children,
}: PropsWithChildren<SectionErrorSuspenseProps>) => {
  return (
    <ErrorBoundary
      fallbackRender={({ error }: { error: Error }) => (
        <div
          role="alert"
          className="alert alert-error flex-1 flex justify-between"
        >{`${errorMsg}. Details: ${error}`}</div>
      )}
    >
      <Suspense
        fallback={
          <span className="ml-6 loading loading-dots loading-lg"></span>
        }
      >
        {children}
      </Suspense>
    </ErrorBoundary>
  );
};
