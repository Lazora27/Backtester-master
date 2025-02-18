import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
