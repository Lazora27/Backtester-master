import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
