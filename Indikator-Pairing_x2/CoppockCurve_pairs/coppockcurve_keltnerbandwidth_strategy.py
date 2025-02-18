import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
