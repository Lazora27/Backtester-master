import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'CenterOfGravity': 1.0
        })
    )
