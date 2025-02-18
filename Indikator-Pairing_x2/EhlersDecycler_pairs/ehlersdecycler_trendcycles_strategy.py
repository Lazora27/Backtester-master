import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und TrendCycles
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'TrendCycles': 1.0
        })
    )
