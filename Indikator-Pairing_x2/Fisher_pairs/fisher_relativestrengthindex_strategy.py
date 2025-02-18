import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
