import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AverageTrueRange': 1.0
        })
    )
