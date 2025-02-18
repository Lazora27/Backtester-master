import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DOMDepth
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DOMDepth': 1.0
        })
    )
