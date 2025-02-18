import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
