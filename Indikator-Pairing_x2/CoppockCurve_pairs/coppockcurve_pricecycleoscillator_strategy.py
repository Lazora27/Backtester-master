import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
