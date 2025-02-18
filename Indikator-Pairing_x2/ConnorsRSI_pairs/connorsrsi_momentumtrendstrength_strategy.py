import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
