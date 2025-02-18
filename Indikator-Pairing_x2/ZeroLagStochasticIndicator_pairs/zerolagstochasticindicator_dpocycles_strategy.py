import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagStochasticIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagStochasticIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ZeroLagStochasticIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
