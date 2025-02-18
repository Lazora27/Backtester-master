import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ModifiedRSI': 1.0
        })
    )
