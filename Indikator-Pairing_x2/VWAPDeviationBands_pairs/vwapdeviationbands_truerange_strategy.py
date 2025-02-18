import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und TrueRange
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'TrueRange': 1.0
        })
    )
