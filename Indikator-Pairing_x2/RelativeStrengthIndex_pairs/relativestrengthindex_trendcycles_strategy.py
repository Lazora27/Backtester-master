import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
