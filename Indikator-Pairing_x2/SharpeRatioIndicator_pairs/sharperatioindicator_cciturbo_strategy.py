import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
