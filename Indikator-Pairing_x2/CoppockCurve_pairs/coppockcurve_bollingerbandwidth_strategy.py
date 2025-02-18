import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
