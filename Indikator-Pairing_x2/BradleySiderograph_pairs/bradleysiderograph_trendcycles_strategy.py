import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und TrendCycles
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'TrendCycles': 1.0
        })
    )
