import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'VWAPBands': 1.0
        })
    )
