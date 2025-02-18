import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
