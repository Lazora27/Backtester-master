import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'CoppockCurve': 1.0
        })
    )
