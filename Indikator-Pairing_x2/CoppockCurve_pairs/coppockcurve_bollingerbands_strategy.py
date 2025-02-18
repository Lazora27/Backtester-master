import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und BollingerBands
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'BollingerBands': 1.0
        })
    )
