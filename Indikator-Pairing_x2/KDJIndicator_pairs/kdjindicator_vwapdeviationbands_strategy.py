import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
