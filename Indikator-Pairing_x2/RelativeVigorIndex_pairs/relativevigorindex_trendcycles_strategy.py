import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
