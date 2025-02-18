import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ArnaudLegouxMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ArnaudLegouxMovingAverage
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ArnaudLegouxMovingAverage': 1.0
        })
    )
