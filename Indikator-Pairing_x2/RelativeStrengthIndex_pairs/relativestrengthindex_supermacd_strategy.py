import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
