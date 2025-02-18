import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'CycleFinder': 1.0
        })
    )
