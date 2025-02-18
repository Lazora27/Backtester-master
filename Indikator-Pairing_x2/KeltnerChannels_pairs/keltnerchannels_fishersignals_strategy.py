import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und FisherSignals
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'FisherSignals': 1.0
        })
    )
