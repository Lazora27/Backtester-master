import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
