import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
