const HelpText = () => {
  return (
    <div className="px-4 pt-4 lg:pt-10 pb-2">
      <p className=" text-md lg:text-xl">
        Monitor Algorand addresses for any changes in balances. Simply input the
        address below and click "Add". You can refresh the watched addresses by
        clicking the refresh button below. This app currently only works on
        Testnet.
      </p>
      <p className="lg:text-xl mt-4">
        You can find addresses to watch in the{" "}
        <a
          className="link"
          href="https://testnet.explorer.perawallet.app/"
          target="_blank"
        >
          Pera Algorand Explorer
        </a>
        .
      </p>
    </div>
  );
};

export default HelpText;
