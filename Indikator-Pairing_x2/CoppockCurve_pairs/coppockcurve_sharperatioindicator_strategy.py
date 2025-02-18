import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
