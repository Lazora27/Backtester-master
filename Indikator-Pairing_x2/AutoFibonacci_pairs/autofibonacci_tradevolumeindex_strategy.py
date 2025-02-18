import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
