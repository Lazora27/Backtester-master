import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
