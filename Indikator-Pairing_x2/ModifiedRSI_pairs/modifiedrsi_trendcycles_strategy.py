import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TrendCycles': 1.0
        })
    )
