import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
