import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'WeightedCycle': 1.0
        })
    )
