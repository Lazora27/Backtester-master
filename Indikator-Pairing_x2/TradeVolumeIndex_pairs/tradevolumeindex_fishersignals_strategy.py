import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
