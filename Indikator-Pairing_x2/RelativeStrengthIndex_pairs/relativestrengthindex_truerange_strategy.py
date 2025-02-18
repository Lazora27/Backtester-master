import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'TrueRange': 1.0
        })
    )
