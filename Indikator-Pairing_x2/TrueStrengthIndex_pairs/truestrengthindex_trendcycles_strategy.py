import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
