import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
