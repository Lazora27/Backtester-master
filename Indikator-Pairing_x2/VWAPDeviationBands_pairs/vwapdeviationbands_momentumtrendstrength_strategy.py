import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
