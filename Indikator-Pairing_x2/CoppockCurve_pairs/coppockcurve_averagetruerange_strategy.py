import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'AverageTrueRange': 1.0
        })
    )
