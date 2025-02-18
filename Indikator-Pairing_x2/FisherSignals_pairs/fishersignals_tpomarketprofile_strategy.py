import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
