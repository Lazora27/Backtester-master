import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
