import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
