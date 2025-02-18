import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
