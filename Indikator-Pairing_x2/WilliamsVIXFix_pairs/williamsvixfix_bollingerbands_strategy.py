import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und BollingerBands
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'BollingerBands': 1.0
        })
    )
