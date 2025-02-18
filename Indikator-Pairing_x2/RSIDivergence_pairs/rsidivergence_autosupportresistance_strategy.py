import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AutoSupportResistance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AutoSupportResistance
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AutoSupportResistance': 1.0
        })
    )
