import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
