import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und BollingerBands
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'BollingerBands': 1.0
        })
    )
