import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
