import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
